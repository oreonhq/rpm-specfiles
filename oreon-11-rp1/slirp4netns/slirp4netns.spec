%global source0_hash a27ed4c7311616516b56015cc74fa06c6431f5c8ebadaf331c0e08150d1a84ce
Name: slirp4netns
Version: 1.3.5
Release:        1%{?dist}
License: GPL-2.0-only
Summary:        slirp for network namespaces
URL: https://github.com/rootless-containers/%{name}
Source0:        https://github.com/rootless-containers/slirp4netns/archive/refs/tags/v1.3.5.tar.gz#/slirp4netns-1.3.1.tar.gz
ExclusiveArch: %{golang_arches_future}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  go-md2man
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libslirp-devel
BuildRequires:  make
# /oreon:deps
%description
slirp for network namespaces, without copying buffers across the namespaces.

%package devel
Summary: %{summary}
BuildArch: noarch
%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man
%install
make DESTDIR=%{buildroot} install install-man
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{!?_licensedir:%global license %doc}
%files -f %{oreon_filedir}/main.list
%files -n slirp4netns-devel -f %{oreon_filedir}/slirp4netns-devel.list

%changelog

%autochangelog
