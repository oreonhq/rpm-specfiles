%global source0_hash fa7fa2bbf2f627dd2d0fdb958bd8ec4527231254c120a8b4322405d8a4e3d12b

Name: sloccount
Summary: Measures source lines of code (SLOC) in programs
Version: 2.26
Release: 44%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.dwheeler.com/sloccount/sloccount-%{version}.tar.gz
URL: https://sourceforge.net/projects/sloccount/
BuildRequires: make
BuildRequires: flex
BuildRequires: perl-generators
BuildRequires: gcc

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for counting
physical source lines of code (SLOC) in potentially large software systems.

SLOCCount can be used to generate reports in different formats for use
by report-generating tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
make CC="${CC:-gcc} ${RPM_OPT_FLAGS} ${RPM_LD_FLAGS}"

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
make install_programs PREFIX=${RPM_BUILD_ROOT}%{_prefix}
make install_man PREFIX=${RPM_BUILD_ROOT}%{_prefix}
# the sloccount makefile doesn't -m 644 on install for man page
chmod 644 ${RPM_BUILD_ROOT}%{_mandir}/man1/sloccount.1.gz
# Duplicate files can actually just be symlinks
cmp ${RPM_BUILD_ROOT}%{_bindir}/java_count ${RPM_BUILD_ROOT}%{_bindir}/c_count && rm ${RPM_BUILD_ROOT}%{_bindir}/java_count && ln -s c_count ${RPM_BUILD_ROOT}%{_bindir}/java_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/tcl_count && rm ${RPM_BUILD_ROOT}%{_bindir}/tcl_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/tcl_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/sed_count && rm ${RPM_BUILD_ROOT}%{_bindir}/sed_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/sed_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/ruby_count && rm ${RPM_BUILD_ROOT}%{_bindir}/ruby_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/ruby_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/makefile_count && rm ${RPM_BUILD_ROOT}%{_bindir}/makefile_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/makefile_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/exp_count && rm ${RPM_BUILD_ROOT}%{_bindir}/exp_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/exp_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/csh_count && rm ${RPM_BUILD_ROOT}%{_bindir}/csh_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/csh_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/awk_count && rm ${RPM_BUILD_ROOT}%{_bindir}/awk_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/awk_count

%files
%doc sloccount.html README ChangeLog COPYING TODO
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
