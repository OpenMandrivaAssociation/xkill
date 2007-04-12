Name: xkill
Version: 1.0.1
Release: %mkrel 3
Summary: Kill a client by its X resource
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xkill is a utility for forcing the X server to close connections to clients.
This program is very dangerous, but is useful for aborting programs that have
displayed undesired windows on a user's screen.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkill
%{_mandir}/man1/xkill.1x.bz2


