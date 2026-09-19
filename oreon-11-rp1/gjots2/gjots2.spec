%global source0_hash 815d66f3d344ffb3dca4d8d4a1e69229160cee9c9d940d50d899d2b5ec5d9e11

# -*-Mode: rpm-spec -*-

Name:    gjots2
Version: 3.2.1
Release: 14%{?dist}
Summary: A hierarchical note jotter - organize your ideas, notes, facts in a tree
License: GPL-2.0-only
URL:     http://bhepple.freeshell.org/gjots
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: python3-gobject
Requires: gtk3

# epel has gtksourceview3 only. f-31/2 also have gtksourceview4. Maybe use weak dependencies?
Requires: gtksourceview3

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

%generate_buildrequires
%pyproject_buildrequires

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files -f gjots2.lang
%license COPYING
%doc AUTHORS ChangeLog README doc/gjots2.gjots
%doc %lang(en_US) doc/gjots2.en_US.gjots
%doc %lang(fr) doc/gjots2.fr.gjots
%doc %lang(nb) doc/gjots2.nb.gjots
%doc %lang(no) doc/gjots2.no.gjots
%doc %lang(ru) doc/gjots2.ru.gjots
%doc %lang(es) doc/gjots2.es.gjots
%{_bindir}/gjots2
%{_bindir}/gjots2org
%{_bindir}/org2gjots
%{_bindir}/gjots2html*
%{_bindir}/gjots2docbook
%{_bindir}/docbook2gjots
%{_bindir}/gjots2emacs
%{_bindir}/gjots2lpr
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info
%{_datadir}/%{name}/
%{_datadir}/pixmaps/gjots2.png
%{_datadir}/metainfo/gjots2.metainfo.xml
%{_datadir}/applications/*gjots2.desktop
%{_datadir}/glib-2.0/schemas/org.gtk.gjots2.gschema.xml
%{_mandir}/man1/%{name}*
%{_mandir}/man1/docbook2gjots*

%changelog
%autochangelog
