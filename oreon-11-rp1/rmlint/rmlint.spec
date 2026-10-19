%global source0_hash 8ffdbd5d09d15c8717ae55497e90d6fa46f085b45ac1056f2727076da180c33e
%undefine _package_note_file
Name:           rmlint
Version:        2.10.3
Release:        1%{?dist}
Summary:        Find space waste and other broken things on your filesystem
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND (CC0-1.0 OR Apache-2.0 OR OpenSSL) AND LicenseRef-Callaway-Public-Domain
URL:            https://rmlint.rtfd.org
Source0:        https://github.com/sahib/rmlint/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Add-RPM_BUILD_ROOT-to-env.patch
Provides:       bundled(blake2)
Provides:       bundled(sha3)
Provides:       bundled(xxhash)
Provides:       bundled(metrohash)
Provides:       bundled(murmurhash3)
Obsoletes:      %{name} < 2.10.3
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libblkid-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  scons
BuildRequires:  sqlite-devel
# /oreon:deps
%package gui
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gtksourceview4
Obsoletes:      %{name} < 2.10.3
%description gui
rmlint-gui (a.k.a. Shredder) is a graphical user interface to rmlint.
It uses rmlint to find space waste and other broken things on your filesystem
and offers to remove them.

%description
rmlint finds space waste and other broken things and offers to remove it.
It is an extremely fast tool to remove duplicates from your filesystem.

%global rmlint_scons_flags --prefix="%{buildroot}%{_prefix}" --actual-prefix="%{_prefix}" --libdir="%{_lib}" --without-compile-glib-schemas DEBUG=1 SYMBOLS=1 VERBOSE=1

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for f in `find gui/shredder -name "*.py"`; do
    sed '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

desktop-file-edit \
	--set-key "Exec" --set-value "shredder" \
	--remove-key "TryExec" \
	gui/shredder.desktop

%build

scons config %{?_smp_mflags} %{rmlint_scons_flags}
scons
%install
scons install %{rmlint_scons_flags}
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/shredder.desktop
%files -f %{oreon_filedir}/main.list
%files -n rmlint-gui -f %{oreon_filedir}/rmlint-gui.list

%changelog

%autochangelog
