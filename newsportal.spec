Summary:	News portal is a PHP based newsreader
Summary(de):	PHP-Skript, welches den Zugriff auf Newsgruppen über Web ermöglicht
Summary(pl):	Skrypt w PHP umo¿liwiaj±cy czytanie newsów przez przegl±darkê
Name:		newsportal
Version:	0.36
Release:	3
License:	GPL
Group:		Networking/News
Source0:	http://florian-amrhein.de/nw/newsportal/download/%{name}-%{version}.tar.gz
# Source0-md5:	9f93d2b7e4f9dcf1eeca90d9477b4a68
Source1:	%{name}-apache.conf
Patch0:		%{name}-path.patch
URL:		http://florian-amrhein.de/newsportal/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php
Requires:	php-pcre
Requires:	php-iconv
Requires:	webserver = apache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
This PHP script enables the access to a newsserver (by NNTP) from a
webpage. It allows you to combine web-forums and newsgroups. The
script is also suitable for presentation of announce newsgroups on web
pages, without having the user notice that he is in fact accessing a
news server.

%description -l de
NewsPortal ist ein PHP-Skript, welches den Zugriff auf Newsgruppen
über Web ermöglicht. Diese Skriptsammlung ermöglicht von einer
Webseite aus den Zugriff auf einen Newsserver (per NNTP). Man kann
damit Webforen und Newsgruppen verbinden, so daß auf ein "Webforum"
auch per NNTP zugegriffen werden kann. Dieses Skript eignet sich auch
für die Präsentation von Announce-Newsgruppen auf Webseiten, ohne daß
der Benutzer merkt, daß er in Wirklichkeit auf einen Newsserver
zugreift.

%description -l pl
NewsPortal pozwala na utworzenie prostego i estetycznego interfejsu do
czytania grup newsowych (przy u¿yciu protoko³u NNTP) przez
przegl±darkê WWW.

%prep
%setup -q -n NewsPortal-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir}/{img,doc,lang,extras/frames,lib},{/var/spool/%{name},%{_sysconfdir}}}

install *.{php,inc,txt,css} $RPM_BUILD_ROOT%{_appdir}
install img/* $RPM_BUILD_ROOT%{_appdir}/img
install lang/* $RPM_BUILD_ROOT%{_appdir}/lang
install lib/* $RPM_BUILD_ROOT%{_appdir}/lib
install extras/frames/* $RPM_BUILD_ROOT%{_appdir}/extras/frames
mv $RPM_BUILD_ROOT%{_appdir}/config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/config.php
mv $RPM_BUILD_ROOT%{_appdir}/groups.txt $RPM_BUILD_ROOT%{_sysconfdir}/groups.txt
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- newsportal < 0.36-1.1
# location before r1.16
for i in groups.txt config.inc.php; do
	if [ -f /home/services/httpd/html/newsportal/$i.rpmsave ]; then
		mv -f %{_sysconfdir}/$i{,.rpmnew}
		mv -f /home/services/httpd/html/newsportal/$i.rpmsave %{_sysconfdir}/$i
	fi
done
# location before r1.23
if [ -f /etc/%{name}/config.inc.rpmsave ]; then
	mv -f %{_sysconfdir}/config.php{,.rpmnew}
	mv -f /etc/%{name}/config.inc.rpmsave %{_sysconfdir}/config.php
fi
if [ -f /etc/%{name}/groups.txt.rpmsave ]; then
	mv -f %{_sysconfdir}/groups.txt{,.rpmnew}
	mv -f /etc/%{name}/groups.txt.rpmsave %{_sysconfdir}/groups.txt
fi

# no earlier registration. autodetect based on installed webservers
if [ -d /etc/apache/webapps.d ]; then
	/usr/sbin/webapp register apache %{_webapp}
	%service apache reload
fi

if [ -d /etc/httpd/webapps.d ]; then
	/usr/sbin/webapp register httpd %{_webapp}
	%service httpd reload
fi

%files
%defattr(644,root,root,755)
%doc doc/*
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/groups.txt
%{_appdir}
%attr(700,http,http) %dir /var/spool/%{name}
