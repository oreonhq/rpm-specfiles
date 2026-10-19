%global source0_hash c6028d6f2fe882af40c7a47601f6d6b5846eebc1add804097a5942b3b102c2cd
%bcond check 0
%global debug_package %{nil}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/ncruces/go-strftime\\)$|^golang\\(github.com/mattn/go-isatty\\)$
%global goipath         modernc.org/libc
%global forgeurl        https://gitlab.com/cznic/libc
Version:                1.61.6
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
C-runtime services for Go without cgo.}
%global golicenses      LICENSE LICENSE-GO LICENSE-honnef\\\
                        COPYRIGHT-MUSL
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        C-runtime services for Go without cgo
License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/libc-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm -rfv v2/
mv honnef.co/go/netdb/LICENSE LICENSE-honnef

#generate_buildrequires
#go_generate_buildrequires

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
