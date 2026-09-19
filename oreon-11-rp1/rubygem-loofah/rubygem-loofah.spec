%global source0_hash 84ad8281f62b1ba0a8f9b4dac86b362ad15d0ae00591ff3cbd36dd72a9cfffbd

%global gem_name loofah

Name: rubygem-%{gem_name}
Version: 2.22.0
Release: 8%{?dist}
Summary: Manipulate and transform HTML/XML documents and fragments
License: MIT
URL: https://github.com/flavorjones/loofah
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/flavorjones/loofah.git && cd loofah
# git archive -v -o loofah-2.22.0-test.tar.gz v2.22.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix minitest6 compatibility
Patch0:  %{gem_name}-2.22.0-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(nokogiri) >= 1.6.6.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(crass)
BuildArch: noarch

%description
Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri. Loofah also includes some HTML
sanitizers based on `html5lib`'s safelist, which are a specific application of
the general transformation functionality.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
(
cd %{_builddir}
%patch -P0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test .

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md

%changelog
%autochangelog
