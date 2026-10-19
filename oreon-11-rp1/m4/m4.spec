%global source1_hash e8c5fb8a54f98c9f9504423ce99279a4e4365e30010a67e13e099a3e8242b8f2
%global source0_hash f25c6ab51548a73a75558742fb031e0625d6485fe5f9155949d6486a2408ab66
Summary:        GNU macro processor
Name: m4
Version: 1.4.21
Release:        1%{?dist}
License: GPL-3.0-or-later AND GFDL-1.3-or-later AND FSFULLR AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND MIT
Source0:        https://mirrors.kernel.org/gnu/m4/m4-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/m4/m4-%{version}.tar.xz.sig
URL: https://www.gnu.org/software/m4/
%ifarch ppc ppc64
%endif
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
chmod 644 COPYING

%build

%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main

%check

make %{?_smp_mflags} check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.21-1
- Prepare for Oreon 11 (RP1)
