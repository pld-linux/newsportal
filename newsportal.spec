Summary:	News portal is a PHP based newsreader
Summary(de):	PHP-Skript, welches den Zugriff auf Newsgruppen über Web ermöglicht
Summary(pl):	Skrypt w PHP umo¿liwiaj±cy czytanie newsów przez przegl±darkê
Name:		newsportal
Version:	0.33
Release:	1
License:	GPL
Group:		Networking/News
Source0:	http://florian-amrhein.de/nw/newsportal/download/%{name}-%{version}.tar.gz
# Source0-md5:	7c4dc71545f47e92c50a554a3ff09997
Patch0:		%{name}-path.patch
URL:		http://florian-amrhein.de/newsportal/
Requires:	apache
Requires:	php
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
przegl±darkê www.

%prep
%setup -q -n NewsPortal-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/{img,doc,lang,extras/frames,lib},{/var/spool,%{_sysconfdir}}/%{name}}

install *.{php,inc,txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install img/* $RPM_BUILD_ROOT%{_datadir}/%{name}/img
install lang/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
install lib/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
install extras/frames/* $RPM_BUILD_ROOT%{_datadir}/%{name}/extras/frames
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/config.inc
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/groups.txt $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- newsportal < 0.27
echo Please move config files from /home/services/httpd/html/newsportal to
echo %{_sysconfdir}/%{name} and update Your configuration to use new directory.

%files
%defattr(644,root,root,755)
%doc doc/*
%dir %{_sysconfdir}/%{name}
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/config.inc
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/groups.txt
%{_datadir}/%{name}
%attr(700,http,http) %dir /var/spool/%{name}
