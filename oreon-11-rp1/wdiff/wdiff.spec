%global source2_hash 0fe55175b96a8ea1c4b670cc3fe11d56b341e4eff81b161ea49958ae550be6ca
%global source1_hash ba2415eb5511dd9f4e102db78000de8f27c66b021ad51668e3afa499a8869f87
%global source0_hash 29a4457eb0ed35c902e6732d71f25e1d6c7fe7fa0eda0fb6c371ed6779b49fd6
%bcond rebuild_mans 1
Name:           wdiff
Version:        1.2.3
Release:        1%{?dist}
Summary:        Compare files on a word per word basis
License:        GPL-3.0-or-later AND Latex2e
URL:            https://www.gnu.org/software/wdiff/
Source0:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Patch:          wdiff-1.2.2-c23.patch
Provides: bundled(gnulib) = 30.5.2012
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gpgverify
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  tex(latex)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
The GNU wdiff program is a front end to diff for comparing files on a word per
word basis. A word is anything between whitespace. This is useful for comparing
two texts in which a few words have been changed and for which paragraphs have
been refilled. It works by creating two temporary files, one word per line, and
then executes diff on these files. It collects the diff output and uses it to
produce a nicer display of word differences between the original files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Fix ISO-8859-1-encoded files
for fn in BACKLOG ChangeLog
do
  iconv --from=ISO-8859-1 --to=UTF-8 "${fn}" > "${fn}.iconv"
  touch -r "${fn}" "${fn}.iconv"
  chmod -v --reference="${fn}" "${fn}.iconv"
  mv -f "${fn}.iconv" "${fn}"
done

%conf
autoreconf -fiv
%configure --enable-experimental="mdiff wdiff2 unify" 

%build

%make_build all
%if %{with rebuild_mans}
rm -v man/mdiff.1 man/wdiff.1 man/wdiff2.1 man/unify.1
%make_build -C man mdiff.1 wdiff.1 wdiff2.1 unify.1
%endif
rm -v doc/wdiff.info
%make_build -C doc info html pdf
%install
%make_install
find '%{buildroot}' -type f -name '*gnulib.mo' -print -delete
rm '%{buildroot}%{_infodir}/dir'
install -d '%{buildroot}%{_pkgdocdir}'
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 \
    ABOUT-NLS \
    AUTHORS \
    BACKLOG \
    ChangeLog \
    NEWS \
    README \
    THANKS \
    TODO
cp -rp doc/wdiff.html %{buildroot}%{_pkgdocdir}/html
%find_lang wdiff
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
