Summary:	Utility for viewing/manipulating the MAC address of network interfaces
Summary(pl):	Narzêdzie do ogl±dania/modyfikowania adresów MAC interfejsów sieciowych
Name:		macchanger
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications/Networking
Vendor:		Alvaro Lopez Ortega <alvaro@alobbs.com>
Source0:	http://savannah.nongnu.org/download/macc/%{name}.pkg/1.2.0/%{name}-%{version}.tar.gz
URL:		http://www.alobbs.com/modules.php?op=modload&name=macc&file=index
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- Set specific MAC address of a network interface
- Set the MAC randomly
- Set a MAC of another vendor
- Set another MAC of the same vendor
- Set a MAC of the same kind (eg: wireless card)
- Display a vendor MAC list (today, 900 items) to choose from

%description -l pl
Mo¿liwo¶ci programu:
- ustawianie adresu MAC interfejsu sieciowego,
- ustawianie adresu MAC losowo,
- ustawianie adresu MAC innego producenta,
- ustawianie innego adresu MAC tego samego producenta,
- ustawianie MAC-a tego samego typu (np. karta bezprzewodowa),
- wy¶wietlanie listy MAC-ów danego producenta, do wyboru.

%prep
%setup -q -n %{name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(755,root,root) %{_bindir}/macchanger
%{_datadir}/%{name}
%{_mandir}/man1/*
