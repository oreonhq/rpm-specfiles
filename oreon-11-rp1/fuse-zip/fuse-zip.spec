%global source0_hash 3dd0be005677442f1fd9769a02dfc0b4fcdd39eb167e5697db2f14f4fee58915

Name:           fuse-zip
Version:        0.7.2
Release:        13%{?dist}
Summary:        Filesystem to navigate, extract, create and modify ZIP archives
Summary(ru):    Пользовательская ФС для работы с ZIP архивами

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://bitbucket.org/agalanin/fuse-zip/
Source0:        https://bitbucket.org/agalanin/fuse-zip/downloads/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libzip-devel
BuildRequires:  fuse-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  make
Requires:       fuse

%description
fuse-zip is a FUSE file system to navigate, extract, create and modify
ZIP archives based in libzip implemented in C++.

With fuse-zip you really can work with ZIP archives as real directories.
Unlike KIO or Gnome VFS, it can be used in any application without
modifications.

Unlike other FUSE filesystems, only fuse-zip provides write support
to ZIP archives. Also, fuse-zip is faster that all known implementations
on large archives with many files.

%description -l ru
fuse-zip - это файловая система для навигации, извлечения, создания и
модификации ZIP архивов, основанная на libzip и написанная на C++.

Используя fuse-zip, вы можете работать с ZIP архивами как с обычными
директориями. В отличие от KIO или Gnome VFS это может быть использовано
в любых приложениях без каких-либо модификаций.

fuse-zip предоставляет полноценную поддержку записи в ZIP архивы. И является
самой быстрой имплементацией при работе с большими архивами со множеством
файлов.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i '/CXXFLAGS=.*/d' lib/Makefile
sed -i '/CXXFLAGS=.*/d' Makefile
sed -i "s|prefix=/usr/local|prefix=%{_prefix}|" Makefile

%build
%set_build_flags
%make_build

%install
%make_install

%files
%doc README.md changelog
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
