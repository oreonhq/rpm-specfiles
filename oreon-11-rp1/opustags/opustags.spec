%global source0_hash 703096e9c41481e30ab90eefdd8fafc4c3a138998b3f8281aa4f023e7058bc86
Name:           opustags
Version:        1.10.1
Release:        1%{?dist}
Summary:        Ogg Opus tags editor
License:        BSD-3-Clause
URL:            https://github.com/fmang/opustags
Source0:        https://github.com/fmang/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          0001-Fix-out-of-bounds-access.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ffmpeg-free
BuildRequires:  gcc-c++
BuildRequires:  libogg-devel
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# /oreon:deps
%description
Opustags allows you to view and edit Ogg Opus comments. It supports the
following features:
* interactive editing using your preferred text editor,
* batch editing with command-line flags,
* tags exporting and importing through text files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm -r %{buildroot}/%{_docdir}/opustags
%oreon_autofiles main

%check

%cmake_build --target check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
