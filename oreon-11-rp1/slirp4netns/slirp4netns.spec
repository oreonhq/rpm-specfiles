Name: slirp4netns
Version: 1.3.1
Release: %autorelease
License: GPL-2.0-only
Summary: slirp for network namespaces
URL: https://github.com/rootless-containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
ExclusiveArch: %{golang_arches_future}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git-core
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libslirp-devel
BuildRequires: make

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
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Import
