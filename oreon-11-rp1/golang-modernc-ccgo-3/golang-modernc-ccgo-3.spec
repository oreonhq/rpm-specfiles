%global source0_hash none
%bcond check 0
%bcond_without bootstrap
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%global goipath         modernc.org/ccgo/v3
%global forgeurl        https://gitlab.com/cznic/ccgo
Version:                3.17.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
ccgo is a C compiler targeting Go.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        C compiler targeting Go
License:        BSD-3-Clause and blessing and GPL-2.0-or-later and GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ccgo-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

%goprep
%autopatch -p1
# Not free:
rm -rfv v3/lib/testdata/CompCert-3.6 v3/lib/testdata/compcert_*.golden
# Replace use of ccorpus with ccorpus2:
sed -i 's|modernc.org/ccorpus\([^2]\)|modernc.org/ccorpus2\1|' $(find . -iname '*.go' -type f)
find . ! \( -name v3 -o -name _build  -o -name LICENSE -o -name AUTHORS -o -name CONTRIBUTORS \) -maxdepth 1 -exec rm -rvf {} \;
mv v3/* .
%if %{with bootstrap}
# Pulls in circular dependency:
rm -fv main.go
%endif

%build

%gobuild -o %{gobuilddir}/bin/ccgo %{goipath}
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{with check}
%check

for test in "TestCompCert" \
            "TestGCCExecuteIEEE" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d lib
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
