%global source0_hash 07f6f7342b7febe4313fc2c2542ad93d64fe20ad8717200109f105a826f5fd37
%global _hardened_build 1
%global gawk_api_major 3
%global gawk_api_minor 2
Name:             gawk
Summary:        The GNU version of the AWK text processing utility
Version:          5.4.1
Release:        1%{?dist}
License:          GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
URL:              https://www.gnu.org/software/gawk/
Source0:        https://mirrors.kernel.org/gnu/gawk/gawk-%{version}.tar.xz
Source1:          LICENSE.GPLv2
Source2:          LICENSE.LGPLv2
Source3:          LICENSE.BSD
Provides:         /bin/awk
Provides:         /bin/gawk
Provides:         gawk(abi) = %{gawk_api_major}.%{gawk_api_minor}
Requires:         filesystem >= 3
# oreon:deps
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  git
BuildRequires:  glibc-all-langpacks
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  readline-devel
BuildRequires:  texinfo-tex
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
# /oreon:deps
%description
The gawk package contains the GNU version of AWK text processing utility. AWK is
a programming language designed for text processing and typically used as a data
extraction and reporting tool.

The gawk utility can be used to do quick and easy text pattern matching,
extracting or reformatting. It is considered to be a standard Linux tool for
text processing.

# === SUBPACKAGES =============================================================

%package devel
Summary:          Header file for gawk extensions development
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description devel
This subpackage provides /usr/include/gawkapi.h header file, which contains
definitions for use by extension functions calling into gawk. For more info
about gawk extensions, please refer to `The GNU Awk User's Guide`.

However, unless you are developing an extension to gawk, you most likely do not
need this subpackage.

# ---------------

%package doc
Summary:          Additional documentation for gawk utility
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch
%description doc
The base package of gawk comes pre-installed with `GAWK: Effective AWK
Programming` and `TCP/IP Internetworking with gawk` user's guides, and you can
access them via info pages.

However, this way of displaying information is less convenient for printing or
displaying images. Therefore, this doc subpackage can provide you with HTML, PDF
and PS versions of those documents, which might be useful when you need to
access them regularly, and/or when you do not have access to Internet.

# ---------------

%package all-langpacks
Summary: 	  Additional localisation files for gawk utility
Supplements: %{name} = %{version}-%{release}
Conflicts: %{name} < 5.0.1-8
%description all-langpacks
The base package of gawk supports only the english localisation. This subpackage
contains additional localisation files.

# === BUILD INSTRUCTIONS ======================================================

# Call the 'autosetup' macro to prepare the environment, but do not patch the
# source code yet -- we need to copy the LICENSE.* files into the directory:
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N -S git
cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .

# Add and amend the copied files to the initial commit, patch the source code:
git add --all --force .
git commit --all --amend --no-edit > /dev/null
%autopatch -p1

# ---------------

%build

autoreconf --force --verbose
%configure
%make_build
%make_build -C doc pdf
mkdir -p html/gawk html/gawkinet
makeinfo --html -I doc -o html/gawk     doc/gawk.texi
makeinfo --html -I doc -o html/gawkinet doc/gawkinet.texi
%check

make check
%install
%make_install
rm -f %{buildroot}%{_bindir}/gawk-%{version}*
rm -f %{buildroot}%{_infodir}/dir
ln -sf gawk %{buildroot}%{_bindir}/awk
ln -sf gawk.1.gz %{buildroot}%{_mandir}/man1/awk.1.gz
ln -sf /usr/share/awk   %{buildroot}%{_datadir}/gawk
ln -sf /usr/libexec/awk %{buildroot}%{_libexecdir}/gawk
%find_lang %{name}
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/html/gawk/
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/html/gawkinet/
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/eg/data/
install -m 0644 -p html/gawk/*           %{buildroot}%{_docdir}/%{name}/html/gawk/
install -m 0644 -p html/gawkinet/*       %{buildroot}%{_docdir}/%{name}/html/gawkinet/
install -m 0644 -p doc/gawk.{pdf,ps}     %{buildroot}%{_docdir}/%{name}
install -m 0644 -p doc/gawkinet.{pdf,ps} %{buildroot}%{_docdir}/%{name}
install -m 0644 -p awklib/eg/data/* %{buildroot}%{_docdir}/%{name}/eg/data/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gawk-devel -f %{oreon_filedir}/gawk-devel.list
%files -n gawk-doc -f %{oreon_filedir}/gawk-doc.list
%files -n gawk-all-langpacks -f %{oreon_filedir}/gawk-all-langpacks.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4.0-2
- Prepare for Oreon 11 (RP1)
