%global source0_hash 96159be799bfa73cdb721b840e9802126e4e03dfc26863db73647204c727f21e

%global gem_name docile

Summary:       Docile keeps your Ruby DSLs tame and well-behaved
Name:          rubygem-%{gem_name}
Version:       1.4.1
Release:       1%{?dist}
License:       MIT
URL:           https://ms-ati.github.com/docile/
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/ms-ati/docile/pull/106
Patch0:        docile-pr106-ruby33-NomethodError-msg.patch
# From https://github.com/ms-ati/docile/pull/108
# Extract patch to support ruby34 error msg syntax change
Patch1:        docile-pr108-support-ruby34-error-msg-syntax.patch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      ruby(rubygems)
%endif
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
# coveralls is now optional for tests
# Add back when coveralls is in Fedora
#BuildRequires: rubygem(coveralls)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(yard)
BuildArch:     noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Provides:      rubygem(%{gem_name}) = %{version}
%endif

%description
Docile turns any Ruby object into a DSL.
Especially useful with the Builder pattern.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.coveralls.yml,.gitignore,.rspec,.ruby-gemset,.ruby-version,.travis.yml,.yard*}

%check
rspec -Ilib spec

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/docile.gemspec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/on_what.rb
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
%autochangelog
