%global source0_hash 12d23156ea4dbe6b37ad48fab2da56ff27b0f6192fb5db210c44eb07bfe6e787
%bcond check 0
%global debug_package %{nil}
%global crate html2text
Name:           rust-html2text0.16
Version:        0.16.7
Release:        1%{?dist}
Summary:        Render HTML as plain text
License:        MIT
URL:            https://crates.io/crates/html2text
Source0:        https://static.crates.io/crates/html2text/html2text-%{version}.crate
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
Summary:        Render HTML as plain text
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+css-devel
Summary:        Render HTML as plain text
BuildArch:      noarch
%description -n %{name}+css-devel

This package contains library source intended for building other packages which
use the "css" feature of the "%{crate}" crate.

%package     -n %{name}+css_ext-devel
Summary:        Render HTML as plain text
BuildArch:      noarch
%description -n %{name}+css_ext-devel

This package contains library source intended for building other packages which
use the "css_ext" feature of the "%{crate}" crate.

%package     -n %{name}+html_trace-devel
Summary:        Render HTML as plain text
BuildArch:      noarch
%description -n %{name}+html_trace-devel

This package contains library source intended for building other packages which
use the "html_trace" feature of the "%{crate}" crate.

%package     -n %{name}+html_trace_bt-devel
Summary:        Render HTML as plain text
BuildArch:      noarch
%description -n %{name}+html_trace_bt-devel

This package contains library source intended for building other packages which
use the "html_trace_bt" feature of the "%{crate}" crate.

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
%files -n rust-html2text0.16-devel -f %{oreon_filedir}/rust-html2text0.16-devel.list

%changelog

%autochangelog
