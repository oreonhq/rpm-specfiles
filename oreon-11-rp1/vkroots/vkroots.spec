%global source0_hash 9487cdefa7f21e4d2dfd5bd8cc67d8ff99ec3c3daaab1f8060ef970c39f31d3b

%global debug_package %{nil}
%global commit 51c32131da197a38c340da2537cbfd695e6ede78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20250716

Name:           vkroots
Version:        0^%{git_date}git%{shortcommit}
Release:        %autorelease
Summary:        A stupid simple method of making Vulkan layers, at home
License:        LGPL-2.1-or-later AND (Apache-2.0 or MIT)
URL:            https://github.com/Joshua-Ashton/vkroots
BuildArch:      noarch

Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch:          https://patch-diff.githubusercontent.com/raw/misyltoad/vkroots/pull/12.patch

BuildRequires:  meson >= 0.58.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  vulkan-headers

%description
vkroots is a framework for writing Vulkan layers that
takes all the complexity/hastle away from you. It's so simple.

%package devel
Summary:        A stupid simple method of making Vulkan layers, at home

%description devel
vkroots is a framework for writing Vulkan layers that
takes all the complexity/hastle away from you. It's so simple.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# Autogenerate the header based on the installed Vulkan Headers
cd gen
./make_vkroots -v -x /usr/share/vulkan/registry/vk.xml

%build
%meson
%meson_build

%install
%meson_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
