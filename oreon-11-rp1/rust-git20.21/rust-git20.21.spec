%global source0_hash ddddbf932745a6be37109b6112d3ee09696106f848449069d3a57bba937ab82e
%bcond check 0
%global debug_package %{nil}
%global crate git2
Name:           rust-git20.21
Version:        0.21.0
Release:        1%{?dist}
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/git2
Source0:        https://static.crates.io/crates/git2/git2-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cred-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+cred-devel

This package contains library source intended for building other packages which
use the "cred" feature of the "%{crate}" crate.

%package     -n %{name}+https-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+https-devel

This package contains library source intended for building other packages which
use the "https" feature of the "%{crate}" crate.

%package     -n %{name}+ssh-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+ssh-devel

This package contains library source intended for building other packages which
use the "ssh" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-sha256-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+unstable-sha256-devel

This package contains library source intended for building other packages which
use the "unstable-sha256" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-libgit2-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+vendored-libgit2-devel

This package contains library source intended for building other packages which
use the "vendored-libgit2" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-openssl-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+vendored-openssl-devel

This package contains library source intended for building other packages which
use the "vendored-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Bindings to libgit2 for interoperating with git repositories. This li...
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-git20.21-devel -f %{oreon_filedir}/rust-git20.21-devel.list

%changelog

%autochangelog
