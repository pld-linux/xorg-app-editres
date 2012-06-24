# $Rev: 3340 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	editres application
Summary(pl):	Aplikacja editres
Name:		xorg-app-editres
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/editres-%{version}.tar.bz2
# Source0-md5:	bce22581f716ff11e9ec7d4b2c425d63
Patch0:		editres-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/editres-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
editres application.

%description -l pl
Aplikacja editres.


%prep
%setup -q -n editres-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.*
