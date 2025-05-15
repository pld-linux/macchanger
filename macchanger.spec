Summary:	Utility for viewing/manipulating the MAC address of network interfaces
Summary(pl.UTF-8):	Narzędzie do oglądania/modyfikowania adresów MAC interfejsów sieciowych
Name:		macchanger
Version:	1.7.0
Release:	1
License:	GPL v2+
Group:		Applications/Networking
#Source0Download: https://github.com/alobbs/macchanger/releases
Source0:	https://github.com/alobbs/macchanger/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ca56f16142914337391dac91603eb332
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/macchanger
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- Set specific MAC address of a network interface
- Set the MAC randomly
- Set a MAC of another vendor
- Set another MAC of the same vendor
- Set a MAC of the same kind (eg: wireless card)
- Display a vendor MAC list (today, 900 items) to choose from

%description -l pl.UTF-8
Możliwości programu:
- ustawianie adresu MAC interfejsu sieciowego,
- ustawianie adresu MAC losowo,
- ustawianie adresu MAC innego producenta,
- ustawianie innego adresu MAC tego samego producenta,
- ustawianie MAC-a tego samego typu (np. karta bezprzewodowa),
- wyświetlanie listy MAC-ów danego producenta, do wyboru.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/macchanger
%{_datadir}/%{name}
%{_mandir}/man1/macchanger.1*
%{_infodir}/macchanger.info*
