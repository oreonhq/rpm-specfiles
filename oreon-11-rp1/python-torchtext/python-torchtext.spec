%global source0_hash fe4eb4b361388ef7840dcad117ae95b32252db5520c4eb2b3bead627468fbdf2
%global pypi_name torchtext
%global pypi_version 0.18.0
Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Data loaders and abstractions for language processing, powered by PyTorch
%bcond_with test
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/pytorch/text
Source0:        https://github.com/pytorch/text/archive/refs/tags/v%{version}.tar.gz#/text-%{version}.tar.gz
Patch0:         0001-Prepare-torchtext-setup-for-fedora.patch
Patch1:         0001-Prepare-torchtext-cmake-for-Fedora.patch
ExclusiveArch:  x86_64 aarch64
%global toolchain gcc
%if %{with test}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  python3dist(expecttest)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(parameterized)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tqdm)
BuildRequires:  re2-devel
BuildRequires:  sentencepiece-devel
BuildRequires:  utf8proc-devel
# /oreon:deps
%description
torchtext is a complementary python package to torch, providing torch
with text processing functionality needed for AI.

%package -n     python3-%{pypi_name}
Summary:        Data loaders and abstractions for language processing, powered by PyTorch
%description -n python3-%{pypi_name}
torchtext is a complementary python package to torch, providing torch
with text processing functionality needed for AI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n text-%{version}

rm -rf third_party/*

%build

%py3_build
%if %{with test}
%check

%pytest -sv
%endif
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-torchtext -f %{oreon_filedir}/python3-torchtext.list

%changelog

%autochangelog
