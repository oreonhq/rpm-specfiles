%global source0_hash 51f74eb0f51cfa9873b85264dfdd5d46e8957ec95b88f0fb762f63d9e164c72e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global tex_texinfo %{_datadir}/texlive/texmf-dist/tex/texinfo
%global __provides_exclude ^perl\\(.*Texinfo.*\\)$
%global __requires_exclude ^perl\\(.*Texinfo.*\\)$

Name: texinfo
Version: 7.3
Release: 1%{?dist}
Summary: Texinfo documentation tools
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/texinfo/
Source0: https://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz
Source1: texinfo-%{version}.tar.xz.sig
Source2: texinfo-key.gpg
Source3: fix-info-dir
Patch0: texinfo-7.1-various-sast-fixes.patch
Patch1: texinfo-7.1-make-tainted-data-safe.patch
Patch2: texinfo-6.7-zstd-compression.patch
Patch3: texinfo-7.3-limits.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gettext
BuildRequires: help2man
BuildRequires: ncurses-devel
BuildRequires: perl
%endif

%description
Texinfo formats documentation for online reading and for print.

%package -n info
Summary: Info document reader
Requires: gzip = 1.15-1%{?dist}
Requires: zstd = 1.5.7-1%{?dist}
Provides: /usr/bin/install-info

%description -n info
info reads Texinfo documents in a terminal. install-info updates the info directory.

%package tex
Summary: TeX support for Texinfo
Requires: texinfo = %{version}-%{release}
Requires: tex(tex)
Requires: tex(epsf.tex)
Requires: /usr/bin/cmp
Requires: /usr/bin/diff
Requires(post): %{_bindir}/texconfig-sys
Requires(postun): %{_bindir}/texconfig-sys
Provides: tex-texinfo
Provides: texlive-texinfo

%description tex
texi2dvi and texi2pdf format Texinfo documents with TeX.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1
mkdir -p contrib
install -Dpm0755 %{SOURCE3} contrib/fix-info-dir

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
mkdir -p %{buildroot}%{tex_texinfo}
install -p -m644 doc/texinfo.tex doc/txi-??.tex %{buildroot}%{tex_texinfo}/
install -Dpm0755 contrib/fix-info-dir %{buildroot}%{_sbindir}/fix-info-dir
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -delete

main=%{_builddir}/texinfo.files
info=%{_builddir}/info.files
tex=%{_builddir}/texinfo-tex.files
: > "$main"
: > "$info"
: > "$tex"
find %{buildroot} \( -type f -o -type l \) | sort | while read -r path; do
  rel=${path#%{buildroot}}
  case "$rel" in
    %{_mandir}/*|%{_infodir}/*)
      dir=$(dirname "$rel")
      base=$(basename "$rel")
      base=${base%.gz}
      line="$dir/${base}*"
      ;;
    *)
      line="$rel"
      ;;
  esac
  case "$rel" in
    %{_bindir}/info|%{_sbindir}/install-info|%{_sbindir}/fix-info-dir|%{_infodir}/info-stnd.info*|%{_mandir}/*/info.1*|%{_mandir}/*/install-info.1*|%{_mandir}/*/info.5*)
      echo "$line" >> "$info"
      ;;
    %{_bindir}/texindex|%{_bindir}/texi2dvi|%{_bindir}/texi2pdf|%{_bindir}/pdftexi2dvi|%{tex_texinfo}/*|%{_mandir}/*/texindex.1*|%{_mandir}/*/texi2dvi.1*|%{_mandir}/*/texi2pdf.1*|%{_mandir}/*/pdftexi2dvi.1*)
      echo "$line" >> "$tex"
      ;;
    *)
      echo "$line" >> "$main"
      ;;
  esac
done
sort -u -o "$main" "$main"
sort -u -o "$info" "$info"
sort -u -o "$tex" "$tex"

%post tex
%{_bindir}/texconfig-sys rehash

%postun tex
%{_bindir}/texconfig-sys rehash

%transfiletriggerin -n info -- %{_infodir}
if [ -f %{_infodir}/dir ]; then
  %{_sbindir}/fix-info-dir %{_infodir}/dir
else
  %{_sbindir}/fix-info-dir --create %{_infodir}/dir
fi

%transfiletriggerpostun -n info -- %{_infodir}
if [ -f %{_infodir}/dir ]; then
  %{_sbindir}/fix-info-dir --delete %{_infodir}/dir
fi

%files -f %{_builddir}/texinfo.files
%license COPYING

%files -n info -f %{_builddir}/info.files
%license COPYING
%ghost %attr(644,root,root) %{_infodir}/dir
%ghost %attr(644,root,root) %{_infodir}/dir.old

%files tex -f %{_builddir}/texinfo-tex.files
%license COPYING
