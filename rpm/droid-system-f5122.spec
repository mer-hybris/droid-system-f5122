Name:		droid-system-f5122
Version:	0.1
Release:	1
Summary:	Droid system for f5122

License:	Proprietary
Source0:	%{name}-%{version}.tar.bz2

# We just need to modify the build.prop from f5121 a bit, so lets
# build require on that and use the file as a base.
BuildRequires:	droid-system-f5121
# We use the same hal build, thus require f512x
Requires:	droid-system-f512x
# We do not want to install this package ever with the f5121 variant.
Conflicts:      droid-system-f5121

# So that we can have generic dependencies as well.
Provides:       droid-system

%description
%{summary}.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/system
cp /system/build.prop %{buildroot}/system/build.prop
echo "persist.radio.multisim.config=dsds" >> %{buildroot}/system/build.prop

%files
%defattr(-,root,root,-)
/system/build.prop

