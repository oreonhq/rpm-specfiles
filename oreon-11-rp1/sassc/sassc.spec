%global testspec_version 3.6.3
%define with_tests 0

Name:           sassc
Version:        3.6.2
Release:        13%{?dist}
Summary:        Wrapper around libsass to compile CSS stylesheet

License:        MIT
URL:            http://github.com/sass/sassc
Source0:        https://github.com/sass/sassc/archive/%{version}/%{name}-%{version}.tar.gz
# Test suite spec. According to this comment from an upstream dev, we should
# not use the release tags on the test spec:
# https://github.com/sass/libsass/issues/2258#issuecomment-268196004
# https://github.com/sass/sass-spec/archive/master.zip
# https://github.com/sass/sass-spec/archive/v%%{testspec_version}.tar.gz
Source1:        sass-spec-libsass-%{testspec_version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 608dc9002b45a91d11ed59e352469ecc05e4f58fc1259fc9a9f5b8f0f8348a03
%global source0_file sassc-3.6.2.tar.gz
# oreon url source checksums end

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  libsass-devel >= %{version}
BuildRequires:  gcc-c++
%if %{with_tests}
# For the test suite
BuildRequires:  ruby
%if 0%{?epel} && 0%{?epel} <= 7
BuildRequires:  rubygem-minitest5
%else
BuildRequires:  rubygem-hrx
BuildRequires:  rubygem-minitest
%endif
%endif

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sassc-3.6.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "608dc9002b45a91d11ed59e352469ecc05e4f58fc1259fc9a9f5b8f0f8348a03" || { echo "oreon: Source0 SHA256 mismatch for sassc-3.6.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -a 1
mv sass-spec-libsass-%{testspec_version} sass-spec
autoreconf -fiv


%build
%configure
%make_build 


%install
%make_install

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

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.2-13
- Import
