%global source0_hash 815d66f3d344ffb3dca4d8d4a1e69229160cee9c9d940d50d899d2b5ec5d9e11
Name:    gjots2
Version: 3.2.1
Release:        14%{?dist}
Summary:        A hierarchical note jotter - organize your ideas, notes, facts in a tree
License: GPL-2.0-only
URL:     http://bhepple.freeshell.org/gjots
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
BuildArch: noarch
Requires: python3-gobject
Requires: gtk3
Requires: gtksourceview3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gjots2 = %{version}-%{release}
# /oreon:deps
%description

gjots2 ("gee-jots" or, if you prefer, "gyachts"!) is a way to marshal
and organize your text notes in a convenient, hierarchical way. For
example, use it for all your notes on Unix, personal bits and pieces,
recipes and even PINs and passwords (encrypted with ccrypt(1), gpg(1)
or openssl(1)).

You can also use it to "mind-map" your compositions - write down all
your thoughts and then start to organize them into a tree. By
manipulating the tree you can easily reorder your thoughts and
structure them appropriately.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Convert to utf-8
for file in doc/man/man1/*.1; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}%{_datadir}/doc/gjots2-%{version}/
for file in $(find po/ -name gjots2.mo | sed 's|po/||') ; do
  install -Dpm0644 po/$file %{buildroot}%{_datadir}/locale/$file
done
%find_lang %{name}
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications              \
        --remove-category Application                           \
        %{name}.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files

%changelog

%autochangelog
