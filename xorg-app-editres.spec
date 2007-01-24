Summary:	editres application - dynamic resource editor for X Toolkit applications
Summary(pl):	Aplikacja editres - edytor dynamicznych zasobów dla aplikacji Xt
Name:		xorg-app-editres
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/editres-%{version}.tar.bz2
# Source0-md5:	a25f931cc6c8d03daaed434f5db5df2d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
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

%description -l pl
editres to narzêdzie pozwalaj±ce u¿ytkownikom i programistom aplikacji
ogl±daæ pe³n± hierarchiê widgetów dowolnej aplikacji Xt (X Toolkitu)
porozumiewaj±cej siê protoko³em Editres. Ponadto editres pomaga
u¿ytkownikom tworzyæ opisy zasobów, pozwala nak³adaæ zasoby na
aplikacje i dynamicznie ogl±daæ wyniki. Kiedy u¿ytkownik jest
zadowolony z zasobów, editres do³±cza ³añcuch zasobów do pliku X
Resources u¿ytkownika.

%prep
%setup -q -n editres-%{version}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/editres
%{_datadir}/X11/app-defaults/Editres*
%{_mandir}/man1/editres.1x*
