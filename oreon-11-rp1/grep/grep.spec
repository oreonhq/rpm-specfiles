%global source0_hash none

%global source2_key_fpr 155D3FC500C834486D1EEA677FD9FCCB000BEEEE

Summary: Pattern matching utilities
Name: grep
Version: 3.12
Release: 3%{?dist}
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GFDL-1.3-no-invariants-or-later
URL: https://www.gnu.org/software/grep/

Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        grep-keyring.gpg
Source3: colorgrep.sh
Source4: colorgrep.csh
Source5: GREP_COLORS
Source6: grepconf.sh

# upstream ticket 39445
Patch: grep-3.5-help-align.patch
# upstream ticket 77800
Patch: grep-3.12-test-write-error-msg-drop.patch

BuildRequires: gcc
BuildRequires: pcre2-devel
BuildRequires: texinfo
BuildRequires: gettext
BuildRequires: autoconf
BuildRequires: automake

# temporal for the gnulib patch
BuildRequires: gettext-devel

Buildrequires: glibc-all-langpacks
BuildRequires: perl(FileHandle)
BuildRequires: make
BuildRequires: gnupg2
# https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)
# for backward compatibility (rhbz#1540485)
Provides: /bin/grep
Provides: /bin/fgrep
Provides: /bin/egrep

%description
The GNU versions of commonly used grep utilities. Grep searches through
textual input for lines which contain a match to a specified pattern and then
prints the matching lines. GNU's grep utilities include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every system.

%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%global BUILD_FLAGS $RPM_OPT_FLAGS

# Currently gcc on ppc uses double-double arithmetic for long double and it
# does not conform to the IEEE floating-point standard. Thus force
# long double to be double and conformant.
%ifarch ppc ppc64
%global BUILD_FLAGS %{BUILD_FLAGS} -mlong-double-64
%endif

%configure --without-included-regex --disable-silent-rules CFLAGS="%{BUILD_FLAGS}"
%make_build

%install
%make_install
gzip $RPM_BUILD_ROOT%{_infodir}/grep*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}
install -Dpm 755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/grepconf.sh

%find_lang %name

%check
make check

%files -f %{name}.lang
%doc AUTHORS THANKS TODO NEWS README
%license COPYING

%{_bindir}/*
%config(noreplace) %{_sysconfdir}/profile.d/colorgrep.*sh
%config(noreplace) %{_sysconfdir}/GREP_COLORS
%{_infodir}/*.info*.gz
%{_mandir}/*/*
%{_libexecdir}/grepconf.sh

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12-3
- Prepare for Oreon 11 (RP1)
