%global source0_hash 9cd8913293572709e122a7c7fa1463fb0e0cf9b38f1d3bf633939564d8cc6245
%bcond check 0
%{!?_pam_moduledir:%global _pam_moduledir %{_libdir}/security}
%{!?_pam_vendordir:%global _pam_vendordir %{_datadir}/pam.d}
%global goipath         github.com/google/fscrypt
Version:                0.3.7
%gometa -f
%global common_description %{expand:
fscrypt is a high-level tool for the management of Linux filesystem encryption.
This tool manages metadata, key generation, key wrapping, PAM integration, and
provides a uniform interface for creating and modifying encrypted directories.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md NEWS.md README.md
Name:           fscrypt
Release:        1%{?dist}
Summary:        Go tool for managing Linux filesystem encryption
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.pam
Patch0:         https://github.com/google/fscrypt/pull/423.patch
Patch1:         https://github.com/google/fscrypt/pull/426.patch
Requires:       (pam_%{name}%{?_isa} = %{version}-%{release} if pam%{?_isa})
# oreon:deps
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  pam-devel
# /oreon:deps
%description %{common_description}

%package -n     pam_%{name}
Summary:        PAM module for managing Linux filesystem encryption
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n pam_%{name} %{common_description}

This is the PAM module associated with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in pam_%{name}; do
  %gobuild -o %{gobuilddir}/lib/$(basename $cmd).so %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_datadir}/bash-completion/completions
install -m 0755 -vp cmd/fscrypt/fscrypt_bash_completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -m 0755 -vd                     %{buildroot}%{_pam_moduledir}
install -m 0755 -vp %{gobuilddir}/lib/pam_%{name}.so %{buildroot}%{_pam_moduledir}/
install -m 0755 -vd                     %{buildroot}%{_pam_vendordir}
install -m 0644 -vp %{SOURCE1}          %{buildroot}%{_pam_vendordir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n pam_fscrypt -f %{oreon_filedir}/pam_fscrypt.list

%changelog

%autochangelog
