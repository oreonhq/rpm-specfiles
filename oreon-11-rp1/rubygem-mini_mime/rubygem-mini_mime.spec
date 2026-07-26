%global source0_hash a00b5ea9f6d6bff503b7715f9814bdbeb2dea6d3843c6edbb07e1c2ac623c68d

# Generated from mini_mime-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mini_mime

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 11%{?dist}
Summary: A lightweight mime type lookup toy
License: MIT
URL: https://github.com/discourse/mini_mime
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not packaged with the gem. You may get them like so:
# git clone --no-checkout https://github.com/discourse/mini_mime
# git -C mini_mime archive -v -o mini_mime-1.1.0-test.txz v1.1.0 test
Source1: %{gem_name}-%{version}-test.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Minimal mime type implementation for use with the mail and rest-client gem.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bench
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
