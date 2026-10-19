%global source0_hash 24e4b0eec5c2b43d0b1de55495ee1ca8fdbd72e36593d9d5f90f7cdc990de32c
%global	gem_name	ensure_valid_encoding
%global	gem_minitest	rubygem(minitest)
Name:		rubygem-%{gem_name}
Version:	0.5.3
Release:        1%{?dist}
Summary:        Replace bad bytes in given encoding with replacement strings
License:	MIT
URL:		https://github.com/jrochkind/ensure_valid_encoding
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
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
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore \
	Gemfile Rakefile \
	*.gemspec \
	test
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:. -e 'gem "minitest", "<5" ; Dir.glob("test/*_test.rb").each {|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ensure_valid_encoding-doc -f %{oreon_filedir}/rubygem-ensure_valid_encoding-doc.list

%changelog

%autochangelog
