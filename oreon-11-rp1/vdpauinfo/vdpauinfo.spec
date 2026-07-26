%global source0_hash fb35038a8c72e40b99aa7baa62795b69c5827ea6cc0a7bfea0fe3fc7c9768530

%global commit d3c5bd63bf8878d59b22d618d2bb5116db392d28
%global gittag 1.5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vdpauinfo
Version:        1.5
Release:        8%{?dist}
Summary:        Tool to query the capabilities of a VDPAU implementation

License:        MIT
URL:            https://gitlab.freedesktop.org/vdpau/vdpauinfo
Source0:        %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libvdpau-devel >= 1.5

%description
Tool to query the capabilities of a VDPAU implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
autoreconf -vif

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/vdpauinfo

%changelog
%autochangelog
