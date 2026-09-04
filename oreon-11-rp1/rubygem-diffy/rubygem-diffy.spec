%global source0_hash 36b42ffbe5138ddc56182107c24ad8d6b066ecfd2876829f391e3a4993d89ae1

%global gem_name diffy

Name:          rubygem-%{gem_name}
Version:       3.4.2
Release:       7%{?dist}
Summary:       A convenient way to diff string in ruby
License:       MIT
URL:           http://github.com/samg/diffy
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch:     noarch

%description
It provides a convenient way to generate a diff from two strings or files.
Instead of reimplementing the LCS diff algorithm Diffy uses battle tested Unix
diff to generate diffs, and focuses on providing a convenient interface,
and getting out of your way.

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
#cleanup
rm -f %{buildroot}%{gem_instdir}/diffy.gemspec

%check
pushd .%{gem_instdir}
  rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/CONTRIBUTORS
%{gem_spec}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%changelog
%autochangelog
