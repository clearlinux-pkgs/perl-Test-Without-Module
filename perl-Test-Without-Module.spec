#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Without-Module
Version  : 0.20
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/C/CO/CORION/Test-Without-Module-0.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CO/CORION/Test-Without-Module-0.20.tar.gz
Summary  : 'Test fallback behaviour in absence of modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Without-Module-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)

%description
NAME
Test::Without::Module - Test fallback behaviour in absence of modules
SYNOPSIS

%package dev
Summary: dev components for the perl-Test-Without-Module package.
Group: Development
Provides: perl-Test-Without-Module-devel = %{version}-%{release}
Requires: perl-Test-Without-Module = %{version}-%{release}

%description dev
dev components for the perl-Test-Without-Module package.


%package perl
Summary: perl components for the perl-Test-Without-Module package.
Group: Default
Requires: perl-Test-Without-Module = %{version}-%{release}

%description perl
perl components for the perl-Test-Without-Module package.


%prep
%setup -q -n Test-Without-Module-0.20
cd %{_builddir}/Test-Without-Module-0.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Without::Module.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Without/Module.pm
