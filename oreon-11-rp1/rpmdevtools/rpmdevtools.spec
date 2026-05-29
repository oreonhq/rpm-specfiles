%global source0_hash 794c97afeb6e81867497b84d2ecfd42dc8c984f59fbab8282f5396419ca7cb9e

Name:           rpmdevtools
Version:        9.6
Release:        14%{?dist}
Summary:        RPM Development Tools

# rpmdev-md5 and rpmdev-setuptree are GPL-2.0-only,
# everything else is GPL-2.0-or-later.
License:        GPL-2.0-or-later AND GPL-2.0-only
URL:            https://pagure.io/rpmdevtools
Source0:        https://releases.pagure.org/rpmdevtools/rpmdevtools-9.6.tar.xz
Source1:        progressbar.py

# Fedora-specific downstream patches
## Force legacy datestamp by default until rhbz#1715412 is resolved
Patch1001:      0001-Force-legacy-datestamp-while-RHBZ-1715412-is-still-a.patch

# RHEL-specific downstream patches
## Remove fakeroot dependency (rhbz#1905465)
Patch2001:      rpmdevtools-9.5-no_qa_robot.patch

BuildArch:      noarch
# help2man, pod2man, *python for creating man pages
BuildRequires:  make
BuildRequires:  help2man
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  perl-generators
# python dependencies for spectool
# spectool is executed for creating man page
BuildRequires:  python3-devel
%if ! 0%{?rhel} || 0%{?oreon}
BuildRequires:  python3dist(progressbar2)
%endif
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rpm)
# emacs-common >= 1:22.3-3 for macros.emacs
BuildRequires:  emacs-common >= 1:22.3-3
BuildRequires:  bash-completion
Requires:       curl
Requires:       diffutils
%if ! 0%{?rhel} || 0%{?oreon}
Requires:       fakeroot
%endif
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       rpm-build >= 4.4.2.3
Requires:       python3dist(argcomplete)
%if ! 0%{?rhel} || 0%{?oreon}
Requires:       python3dist(progressbar2)
%endif
Requires:       python3dist(requests)
Requires:       python3dist(rpm)
Requires:       sed
Requires:       emacs-filesystem
# Optionally support rpmautospec
Recommends:     python%{python3_version}dist(rpmautospec)

%description
This package contains scripts and Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
rpmdev-spectool     Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -N
%autopatch -p1 %{!?rhel:-M2000}
grep -lF "%{_bindir}/python " * \
| xargs sed -i -e "s|%{_bindir}/python |%{_bindir}/python3 |"

%if 0%{?rhel} || 0%{?oreon}
# Let spectool find the bundled progressbar2 implementation
cp %{SOURCE1} .
sed -i \
's|^\(import progressbar\)$|'\
'import sys\n'\
'sys.path.insert(1, "%{_datadir}/rpmdevtools")\n'\
'\1\nsys.path.pop(1)|' \
rpmdev-spectool
%endif


%build
%configure --libdir=%{_prefix}/lib
%make_build


%install
%make_install

echo %%{_datadir}/bash-completion > %{name}.files
[ -d %{buildroot}%{_sysconfdir}/bash_completion.d ] && \
echo %%{_sysconfdir}/bash_completion.d > %{name}.files

for dir in %{_emacs_sitestartdir} ; do
  install -dm 755 %{buildroot}$dir
  ln -s %{_datadir}/rpmdevtools/rpmdev-init.el %{buildroot}$dir
  touch %{buildroot}$dir/rpmdev-init.elc
done

# For backwards compatibility
ln -sr %{buildroot}%{_bindir}/rpmdev-spectool %{buildroot}%{_bindir}/spectool
echo ".so man1/rpmdev-spectool.1" > %{buildroot}%{_mandir}/man1/spectool.1

%if 0%{?rhel} || 0%{?oreon}
cp %{SOURCE1} %{buildroot}%{_datadir}/rpmdevtools/
%py_byte_compile %{python3} %{buildroot}%{_datadir}/rpmdevtools/
%endif


%files -f %{name}.files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_datadir}/rpmdevtools/
%{_bindir}/*
%{_emacs_sitestartdir}/rpmdev-init.el
%ghost %{_emacs_sitestartdir}/rpmdev-init.elc
%{_mandir}/man[18]/*.[18]*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.6-14
- Import
