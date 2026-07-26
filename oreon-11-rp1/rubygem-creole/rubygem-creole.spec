%global source0_hash 951701e2d80760f156b1cb2a93471ca97c076289becc067a33b745133ed32c03

%global gem_name creole

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 27%{?dist}
Summary: Lightweight markup language
# The license was never really clear, but based on the upstream license
# content, we might assune the code is "Ruby OR BSD-2-Cluase" licensed.
# https://github.com/minad/creole/blob/master/LICENSE
# https://github.com/minad/creole/issues/7
License: Ruby OR BSD-2-Clause
URL: https://github.com/minad/creole
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Include the upstream LICENSE file.
Source1: https://raw.githubusercontent.com/minad/creole/d0b49a67465ed70eacd4d88790f9462beb9ed068/LICENSE
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bacon)
BuildArch: noarch

%description
Creole is a lightweight markup language (http://wikicreole.org/).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

install -p -m 0644 %{SOURCE1} .

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
bacon -Ilib test/*_test.rb
popd

%files
%license LICENSE
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/README.creole
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/creole.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
