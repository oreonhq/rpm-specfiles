%global source0_hash d059b292cc9bcee53219ca620a24b35b16b316b2fc193b3e9f5c1298f5a67cb8
%global forgeurl https://github.com/skozina/kabi-dw
%global commitdate 20190729
%global commit bd56a6004d5d409d7d03c386400da3f49a8c4c03
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta
Name:           kabi-dw
Version:        0
Release:        1%{?dist}
Summary:        Detect changes in the ABI between kernel builds
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        https://github.com/skozina/kabi-dw/archive/bd56a6004d5d409d7d03c386400da3f49a8c4c03.tar.gz#/kabi-dw-bd56a6004d5d409d7d03c386400da3f49a8c4c03.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  redhat-rpm-config
# /oreon:deps
%description
The aim of kabi-dw is to detect any changes in the ABI between the successive
builds of the Linux kernel. This is done by dumping the DWARF type information
(the .debug_info section) for the specific symbols into the text files and
later comparing the text files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgesetup

%build

LDFLAGS+=" -z muldefs "
%set_build_flags
%make_build
%install
install -dm 755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0-0.30
- Prepare for Oreon 11 (RP1)
