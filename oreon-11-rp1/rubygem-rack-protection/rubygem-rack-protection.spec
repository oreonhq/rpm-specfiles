%global source0_hash 2ff59892ac0ea557f0d22682f5402f8ab283f4cf2bcc599913e6f26e40ee1024

%global gem_name rack-protection

%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 4.2.1
Release: 2%{?dist}
Summary: Ruby gem that protects against typical web attacks
License: MIT
URL: https://sinatrarb.com/protection/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sinatra/sinatra.git && cd sinatra/rack-protection
# git archive -v -o rack-protection-4.2.1-spec.tar.gz v4.2.1 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(base64)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rack-test)
%endif
BuildArch: noarch

%description
Protect against typical web attacks, works with all Rack apps, including
Rails.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

rspec -rspec_helper spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/License
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rack-protection.gemspec

%changelog
%autochangelog
