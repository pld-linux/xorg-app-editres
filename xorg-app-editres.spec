Summary:	editres application - dynamic resource editor for X Toolkit applications
Summary(pl.UTF-8):	Aplikacja editres - edytor dynamicznych zasobów dla aplikacji Xt
Name:		xorg-app-editres
Version:	1.0.6
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/editres-%{version}.tar.bz2
# Source0-md5:	623322610e4040393e0ff2a69e6612cd
Patch0:		%{name}-format.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
editres is a tool that allows users and application developers to view
the full widget hierarchy of any X Toolkit application that speaks the
Editres protocol. In addition, editres will help the user construct
resource specifications, allow the user to apply the resource to the
application and view the results dynamically. Once the user is happy
with a resource specification editres will append the resource string
to the user's X Resources file.

%description -l pl.UTF-8
editres to narzędzie pozwalające użytkownikom i programistom aplikacji
oglądać pełną hierarchię widgetów dowolnej aplikacji Xt (X Toolkitu)
porozumiewającej się protokołem Editres. Ponadto editres pomaga
użytkownikom tworzyć opisy zasobów, pozwala nakładać zasoby na
aplikacje i dynamicznie oglądać wyniki. Kiedy użytkownik jest
zadowolony z zasobów, editres dołącza łańcuch zasobów do pliku X
Resources użytkownika.

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/editres
%{_datadir}/X11/app-defaults/Editres*
%{_mandir}/man1/editres.1*
