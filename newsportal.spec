Summary:	News portal is a PHP based newsreader
Summary(de):	PHP-Skript, welches den Zugriff auf Newsgruppen über Web ermöglicht
Summary(pl):	Skrypt w PHP umo¿liwiaj±cy czytanie newsów przez przegl±darkê
Name:		newsportal
Version:	0.24pre7
Release:	1
License:	GPL
Group:		Networking/Communication
Source0:	http://florian-amrhein.de/newsportal/download/%{name}-%{version}.tar.gz
URL:		http://florian-amrhein.de/newsportal/
Requires:	apache
Requires:	php
Requires:	php-pcre
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wwwrootdir	/home/httpd
%define		_wwwuser	http
%define		_wwwgroup	http


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
cd $RPM_BUILD_DIR
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
tar -xzf %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/{img,spool,doc,extras/{frames,lang}}
install *.{php,inc,lang,txt} $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal
install img/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/img
install doc/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/doc
install extras/lang/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/extras/lang
install extras/frames/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/extras/frames

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_wwwrootdir}/html/newsportal/*.php
%config(noreplace) %verify(not size mtime md5) %{_wwwrootdir}/html/newsportal/config.inc
%{_wwwrootdir}/html/newsportal/*a*.inc
%{_wwwrootdir}/html/newsportal/*.lang
%{_wwwrootdir}/html/newsportal/*.txt
%{_wwwrootdir}/html/newsportal/img/*
%{_wwwrootdir}/html/newsportal/extras/*
%attr(700,%{_wwwuser},%{_wwwgroup}) %dir %{_wwwrootdir}/html/newsportal/spool
%doc doc/*
