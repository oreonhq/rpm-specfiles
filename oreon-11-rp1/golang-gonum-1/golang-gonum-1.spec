%global source0_hash bc1eb0421c14c1e82e6e71de83d343db5d88ac629ff3c10bbf2cc748c0a686e5
%ifarch x86_64
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         gonum.org/v1/gonum
%global forgeurl        https://github.com/gonum/gonum
Version:                0.9.3
%gometa
%global common_description %{expand:
Gonum is a set of packages designed to make writing numerical and scientific
algorithms productive, performant, and scalable.
Gonum contains libraries for matrices and linear algebra; statistics,
probability distributions, and sampling; tools for function differentiation,
integration, and optimization; network creation and analysis; and more.}
%global golicenses      LICENSE THIRD_PARTY_LICENSES/Bogaert-LICENSE THIRD_PARTY_LICENSES/Boost-LICENSE THIRD_PARTY_LICENSES/Cephes-LICENSE THIRD_PARTY_LICENSES/Fike-LICENSE THIRD_PARTY_LICENSES/Go-LICENSE THIRD_PARTY_LICENSES/Oxford-LICENSE THIRD_PARTY_LICENSES/Probab-LICENSE THIRD_PARTY_LICENSES/Sun-LICENSE
%global godocs          AUTHORS CONDUCT.md CONTRIBUTING.md CONTRIBUTORS README.md README-*.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Set of numeric libraries for Go
License:        MIT and BSD and Boost
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gonum-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(golang.org/x/tools/container/intsets)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
for f in blas diff floats graph integrate lapack mat mathext optimize stat; do
  mv $f/README.md README-$f.md
done

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -t graph
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
