%global source0_hash bed7445617282a766afc58663068fb5360e4e3333a9790ad74ba5f021ea6069a

Name:           cpanspec
Version:        1.78
Release:        57%{?dist}
Summary:        RPM spec file generation utility
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://cpanspec.sourceforge.net/
Source0:        http://sourceforge.net/downloads/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.78-Change-optimize-to-optflags.patch
Patch1:         %{name}-1.78-Strip-any-version-comparison-operator-from-the-perl-BR.patch
Patch2:         %{name}-1.78-Escape-slashes-in-filters.patch
Patch3:         %{name}-1.78-Prefer-dnf-over-repoquery.patch
Patch4:         %{name}-1.78-Fix-build-arguments-for-Build.PL-spec-conformance.patch
Patch5:         %{name}-1.78-Update-licenses-to-SPDX-form.patch
Patch6:         %{name}-1.78-Update_to_actual_fedora_rules.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
Requires:       /usr/bin/curl
Requires:       /usr/bin/dnf
Requires:       rpm-build

%description
cpanspec generates spec files (and, optionally, source or even binary
packages) for Perl modules from CPAN for Fedora.  The quality of the spec
file is our primary concern.  It is assumed that maintainers will need to
do some (hopefully small) amount of work to clean up the generated spec
file to make the package build and to verify that all of the information
contained in the spec file is correct.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%files
%{!?_licensedir:%global license %%doc}
%license Artistic COPYING
%doc BUGS Changes TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
