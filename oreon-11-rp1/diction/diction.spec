%global source0_hash da012fb3a5cba6566d238cda869b0cecdbef0452780c4d368100a840472fd7fc
Name:           diction
Version:        1.14
Release:        1%{?dist}
Summary:        Identifies diction and style errors
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/diction/diction.html
Source0:        http://www.moria.de/~michael/diction/diction-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
Diction and style are two old standard UNIX commands. Diction identifies wordy
and commonly misused phrases. Style analyses surface characteristics of a
document, including sentence length and other readability measures.

These programs cannot help you structure a document well, but they can help to
avoid poor wording and compare the readability (not the understandability!) of
your documents with others. Both commands support English and German documents.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
for FILE in *.1; do
    /usr/bin/iconv -f iso-8859-1 -t utf-8 $FILE > $FILE.utf8
    mv -f $FILE.utf8 $FILE
done
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
