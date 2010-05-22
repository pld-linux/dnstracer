Summary:	DNS query tracer
Summary(pl.UTF-8):	Program śledzący zapytania DNS
Name:		dnstracer
Version:	1.9
Release:	1
Group:		Networking/Utilities
License:	BSD-like
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	7db73ce3070119c98049a617fe52ea84
URL:		http://www.mavetju.org/unix/general.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

Its behaviour is similair to ntptrace(8), which does it for the NTP
protocol.

%description -l pl.UTF-8
Dnstracer rozpoznaje skąd podane serwery DNS pobierają swoje
informacje i podąża za łańcuchem serwerów DNS bezpośrednio do serwera
który zawiera poszukiwane informacje.

Jego zachowanie jest podobne do ntptrace(8), który dokonuje podobnej
operacji korzystając z protokołu NTP.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
rm -f missing
rm -r autom4te.cache
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
%doc CHANGES CONTACT FILES LICENSE
%attr(755,root,root) %{_bindir}/dnstracer
%{_mandir}/man8/dnstracer.8*
