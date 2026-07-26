%global source0_hash none

%global commit 3ccaa1acbd1e092787fa488d046bdcb3762e51ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250530

Name:       unzboot
Version:    0.1~git.%{commitdate}.%{shortcommit}
Release:    3%{?dist}

Summary:    Extracts a kernel vmlinuz image from a EFI application
License:    GPL-2.0-or-later

URL:        https://github.com/eballetbo/unzboot
# Upstream is still under development so they are not tagging releases
# yet. Use the following to do a rebase to a new snapshot:
#
# git archive --format=tar --prefix=${name}-${shortcommit}/ ${shortcommit} | xz > ${name}-${shortcommit}.tar.xz
Source0:       %{name}-%{shortcommit}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: meson
BuildRequires: zlib
BuildRequires: libzstd-devel

%description
The unzboot program extracts a kernel vmlinuz image from
a EFI application that carries the actual kernel image in
compressed form.

%prep
%autosetup -n %{name}-%{shortcommit}
%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/unzboot

%changelog
%autochangelog
