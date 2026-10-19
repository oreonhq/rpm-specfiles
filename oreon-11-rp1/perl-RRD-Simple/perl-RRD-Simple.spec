%global source0_hash 6ddda37bc49adeeb2ccc89d0ef320ea2f3287799fa4186ba9a54d2124efb473f
Name:		perl-RRD-Simple
Version:	1.44
Release:        1%{?dist}
Summary:        Simple interface to create and store data in RRD files
License:	Apache-2.0
URL:		https://metacpan.org/release/RRD-Simple
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NICOLAW/RRD-Simple-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Data::Dumper)
Requires:	perl(File::Copy)
Requires:	perl(File::Temp)
BuildConflicts:	perl(Test::Deep)
%global rrd_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RRDs)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
RRD::Simple provides a simple interface to RRDTool's RRDs module. This module
does not currently offer the fetch method that is available in the RRDs
module. It does, however, create RRD files with a sensible set of default RRA
Round Robin Archive) definitions, and can dynamically add new data source
names to an existing RRD file.

This module is ideal for quick and simple storage of data within an RRD file
if you do not need to, nor want to, bother defining custom RRA definitions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RRD-Simple-%{version}

# Don't want provides/requires from documentation
%global docfilt perl -p -e 's|%{rrd_docdir}\\S+||'
# RRD::Simple version should be from distribution version, not svn revision
%global verfilt perl -p -e 's/(perl\\(RRD::Simple\\) =) \\d+/\\1 %{version}/'
# Apply provides/requires filters
%global provfilt /bin/sh -c "%{docfilt} | %{__perl_provides} | %{verfilt}"
%global __perl_provides %{provfilt}
%global reqfilt /bin/sh -c "%{docfilt} | %{__perl_requires}"
%global __perl_requires %{reqfilt}

%build

AUTOMATED_TESTING=1 perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

LC_ALL=C ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
