%global source0_hash 6e44cfb464e022d47b9a981b1bcbbbc7ad95594270740a56678e56f7ce8c98cd
%bcond check 0
Name:           cargo-rpm-macros
Version:        28.5
Release:        1%{?dist}
Summary:        RPM macros and generators for building Rust packages with cargo
License:        MIT
URL:            https://codeberg.org/rust2rpm/cargo-rpm-macros
Source0:        https://codeberg.org/rust2rpm/%{name}/archive/v%{version}.tar.gz
Patch:          0001-Temporarily-accept-cargo_prep-V-flag-for-spec-compat.patch
BuildArch:      noarch
%if %{with check}
%endif
Obsoletes:      rust-packaging < 24
Provides:       rust-packaging = %{version}-%{release}
Requires:       cargo2rpm >= 0.3.3-4
Requires:       cargo
Requires:       gawk
Requires:       grep
Requires:       rust-srpm-macros
# oreon:deps
BuildRequires:  python3-pytest
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cargo-rpm-macros
%oreon_prep
%build

%install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo-buildsys
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo.attr
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo_vendor.attr
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
pytest -vv
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
