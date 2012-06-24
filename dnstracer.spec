Summary:	dns tracer
Summary(pl):	Program �ledz�cy zapytania DNS
Name:		dnstracer
Version:	1.8
Release:	1
Group:		Applications/Networking
License:	BSD-like
Source0:	http://www.mavetju.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	f7e4102b572d052ca95567a08d9dde0a
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

%description -l pl
Dnstracer rozpoznaje sk�d podane serwery DNS pobieraj� swoje
informacje i pod��a za �a�cuchem serwer�w DNS bezpo�rednio do serwera
kt�ry zawiera poszukiwane informacje.

Jego zachowanie jest podobne do ntptrace(8), kt�ry dokonuje podobnej
operacji korzystaj�c z protoko�u NTP.

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
