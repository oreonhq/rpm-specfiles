%global source0_hash 608dc9002b45a91d11ed59e352469ecc05e4f58fc1259fc9a9f5b8f0f8348a03
%global source1_hash 1c84cad4624980259f00e2f9f8cc42c9b716986511ab6251fbb1547f612818f8
%global testspec_version 3.6.3
%define with_tests 0
Name:           sassc
Version:        3.6.2
Release:        1%{?dist}
Summary:        Wrapper around libsass to compile CSS stylesheet
License:        MIT
URL:            http://github.com/sass/sassc
Source0:        https://github.com/sass/sassc/archive/refs/tags/3.6.2.tar.gz#/sassc-3.6.2.tar.gz
Source1:        https://github.com/sass/sass-spec/archive/refs/tags/libsass-%{testspec_version}.tar.gz#/sass-spec-libsass-%{testspec_version}.tar.gz
%if %{with_tests}
%if 0%{?epel} && 0%{?epel} <= 7
%else
%endif
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -a 1 -n sassc-3.6.2
mv sass-spec-libsass-%{testspec_version} sass-spec
autoreconf -fiv

%build

%configure
%make_build 
%install
%make_install
%oreon_autofiles main
%if %{with_tests}
%check

rm sass-spec/spec/basic/12_pseudo_classes_and_elements.hrx
rm sass-spec/spec/basic/44_bem_selectors.hrx
rm sass-spec/spec/extend-tests/018_test_id_unification.hrx
rm sass-spec/spec/extend-tests/065_test_attribute_unification.hrx
rm sass-spec/spec/extend-tests/066_test_attribute_unification.hrx
rm sass-spec/spec/extend-tests/067_test_attribute_unification.hrx
rm sass-spec/spec/extend-tests/068_test_attribute_unification.hrx
rm sass-spec/spec/extend-tests/070_test_pseudo_unification.hrx
rm sass-spec/spec/extend-tests/071_test_pseudo_unification.hrx
rm sass-spec/spec/extend-tests/074_test_pseudo_unification.hrx
rm sass-spec/spec/extend-tests/087_test_negation_unification.hrx
rm sass-spec/spec/libsass-closed-issues/issue_2520.hrx
ruby sass-spec/sass-spec.rb -c ./%{name} --impl libsass sass-spec/spec
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.2-13
- Import
