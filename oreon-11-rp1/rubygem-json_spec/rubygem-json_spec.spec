%global source0_hash 7a77b97a92c787e2aa3fbc4a1239afc3342c781151dc98cfb81461b3b7cad10f

%global gem_name json_spec

Name:           rubygem-%{gem_name}
Version:        1.1.5
Release:        21%{?dist}
Summary:        Easily handle JSON in RSpec and Cucumber

License:        MIT
URL:            https://github.com/collectiveidea/json_spec
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# only for ruby 2.4+
Patch0:         %{name}-ruby24.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygem(rspec)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(multi_json) < 2
Requires:       rubygem(multi_json) >= 1.0
Requires:       rubygem(rspec) < 4.0
Requires:       rubygem(rspec) >= 2.0
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
RSpec matchers and Cucumber steps for testing JSON content.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%if 0%{?fedora} >= 26
%patch -P0 -p1
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# remove developer-only files
for f in .gitignore .travis.yml Gemfile Rakefile gemfiles/*; do
  rm $f
  sed -i "s|\"$f\"\(.freeze\)\?,\?||g" %{gem_name}.gemspec
done

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec
cucumber --tags "not @fail"
popd

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/features/
%{gem_instdir}/spec/

%changelog
%autochangelog
