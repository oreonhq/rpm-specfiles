%global source1_hash 62d4867d7cfff57a364b745866d798958a90286551fdf45d08df515fa8c79c25
%global source0_hash 2649b27c0e90e632eadcd757be06c6e9a4f48d941de51e7c0f83ff76408a07b9
%global source2_key_fpr 155D3FC500C834486D1EEA677FD9FCCB000BEEEE
Summary:        Pattern matching utilities
Name: grep
Version: 3.12
Release:        1%{?dist}
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GFDL-1.3-no-invariants-or-later
URL: https://www.gnu.org/software/grep/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        grep-keyring.gpg
Source3: colorgrep.sh
Source4: colorgrep.csh
Source5: GREP_COLORS
Source6: grepconf.sh
Patch: grep-3.5-help-align.patch
Patch: grep-3.12-test-write-error-msg-drop.patch
Provides: bundled(gnulib)
Provides: /bin/grep
Provides: /bin/fgrep
Provides: /bin/egrep
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-all-langpacks
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl(FileHandle)
BuildRequires:  texinfo
# /oreon:deps
%description
The GNU versions of commonly used grep utilities. Grep searches through
textual input for lines which contain a match to a specified pattern and then
prints the matching lines. GNU's grep utilities include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every system.

%prep

test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%global BUILD_FLAGS $RPM_OPT_FLAGS
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
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12-3
- Prepare for Oreon 11 (RP1)
