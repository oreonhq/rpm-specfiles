%global source0_hash 0f321d77c20e19b92c39e7471cf986812cbb46659d2af674adc4331ef3f18394
%bcond check 0
%global debug_package %{nil}
%global crate av-scenechange
Name:           rust-av-scenechange
Version:        0.14.1
Release:        1%{?dist}
Summary:        Estimates frames in a video where a scenecut would be ideal
License:        MIT
URL:            https://crates.io/crates/av-scenechange
Source0:        https://static.crates.io/crates/av-scenechange/av-scenechange-%{version}.crate
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
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+binary-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+console-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+console-devel

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%package     -n %{name}+devel-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+devel-devel

This package contains library source intended for building other packages which
use the "devel" feature of the "%{crate}" crate.

%package     -n %{name}+fern-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+fern-devel

This package contains library source intended for building other packages which
use the "fern" feature of the "%{crate}" crate.

%package     -n %{name}+ffmpeg-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+ffmpeg-devel

This package contains library source intended for building other packages which
use the "ffmpeg" feature of the "%{crate}" crate.

%package     -n %{name}+ffmpeg-the-third-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+ffmpeg-the-third-devel

This package contains library source intended for building other packages which
use the "ffmpeg-the-third" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-chrome-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+tracing-chrome-devel

This package contains library source intended for building other packages which
use the "tracing-chrome" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-subscriber-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+tracing-subscriber-devel

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-devel
Summary:        Estimates frames in a video where a scenecut would be ideal
BuildArch:      noarch
%description -n %{name}+vapoursynth-devel

This package contains library source intended for building other packages which
use the "vapoursynth" feature of the "%{crate}" crate.

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
%files -n rust-av-scenechange-devel -f %{oreon_filedir}/rust-av-scenechange-devel.list

%changelog

%autochangelog
