%global source0_hash 24e4b0eec5c2b43d0b1de55495ee1ca8fdbd72e36593d9d5f90f7cdc990de32c

%global	gem_name	ensure_valid_encoding
%if 0%{?fedora} >= 21
%global	gem_minitest	rubygem(minitest4)
%else
%global	gem_minitest	rubygem(minitest)
%endif

Name:		rubygem-%{gem_name}
Version:	0.5.3
Release:	24%{?dist}

Summary:	Replace bad bytes in given encoding with replacement strings
License:	MIT
URL:		https://github.com/jrochkind/ensure_valid_encoding
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	%gem_minitest
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}

%description
Replace bad bytes in given encoding with replacement strings, _or_ 
fail quickly on invalid encodings --  _without_ a transcode to 
a different encoding.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore \
	Gemfile Rakefile \
	*.gemspec \
	test
popd

%check
pushd .%{gem_instdir}
ruby -Ilib:. -e 'gem "minitest", "<5" ; Dir.glob("test/*_test.rb").each {|f| require f}'
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{gem_libdir}
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
