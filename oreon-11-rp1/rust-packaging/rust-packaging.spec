%global source0_hash a4514b547cd305060c0e8ee018c2a0e87b5d203b0230153d4dee70ddcd38bf54

%bcond_without check

Name:           rust-packaging
Version:        26.4
Release:        %autorelease
Summary:        RPM macros and generators for building Rust packages
License:        MIT

URL:            https://pagure.io/fedora-rust/rust-packaging
Source0:        https://pagure.io/fedora-rust/rust-packaging/archive/26.4/rust-packaging-26.4.tar.gz

# cargo_prep -V exists on some EL spec copies; this branch accepts the flag and
# errors only when %%{?fedora} is defined so one macro file can be shared.
Patch0:        0001-Temporarily-accept-cargo_prep-V-flag-for-spec-compat.patch

BuildArch:      noarch

%if %{with check}
BuildRequires:  python3-pytest
%endif

%description
Macros and fileattrs used when building Rust crates into RPMs on this distro.

%if ! 0%{?rhel}
%package -n rust-srpm-macros
Summary:        RPM macros for building Rust projects

%description -n rust-srpm-macros
RPM macros for building source packages for Rust projects.
%endif

%package -n cargo-rpm-macros
Summary:        RPM macros for building projects with cargo

Obsoletes:      rust-packaging < 24
Provides:       rust-packaging = %{version}-%{release}

Requires:       cargo2rpm >= 0.1.8

Requires:       cargo
Requires:       gawk
Requires:       grep

%if ! 0%{?rhel}
Requires:       rust-srpm-macros = %{version}-%{release}
%else
Requires:       rust-srpm-macros
%endif

%description -n cargo-rpm-macros
RPM macros for building projects with cargo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
# nothing to do

%install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust
%if ! 0%{?rhel}
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust-srpm
%endif
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo.attr
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo_vendor.attr

%if %{with check}
%check
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
pytest -vv
%endif

%if ! 0%{?rhel}
%files -n rust-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.rust
%{_rpmmacrodir}/macros.rust-srpm
%endif

%files -n cargo-rpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.cargo
%if 0%{?rhel}
%{_rpmmacrodir}/macros.rust
%endif
%{_fileattrsdir}/cargo.attr
%{_fileattrsdir}/cargo_vendor.attr

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.4-1
- Import rust-packaging 26.4, pagure HTTPS tarball, vendor changelog, cargo_prep patch
